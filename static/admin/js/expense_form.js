function expenseForm() {
    return {
        category: null,
        subcategories: [],
        type: '',
        error: null,
        recurringFields: [
            {name: 'recurring_interval', required: true},
            {name: 'recurring_frequency', required: true},
            {name: 'end_date_0', type: 'datetime', required: true},
            {name: 'end_date_1', type: 'datetime', required: true},
            {name: 'last_occurrence', type: 'datetime', required: false},
            {name: 'next_occurrence', type: 'datetime', required: false}
        ],
        
        init() {
            this.$nextTick(() => {
                const categoryField = document.getElementById('id_category');
                const typeField = document.getElementById('id_type');

                this.setupFieldObserver(categoryField, 'category');
                this.setupFieldObserver(typeField, 'type');

                this.category = categoryField?.value || '';
                this.type = typeField?.value || '';

                if (this.category) {
                    this.fetchSubcategories(this.category);
                }
                
                this.toggleRecurringFields();
            });

            this.$watch('category', value => {
                if (value) {
                    this.fetchSubcategories(value);
                } else {
                    this.subcategories = [];
                    this.updateSubcategoryField();
                }
            });

            this.$watch('type', value => {
                console.log('Type changed to:', value);
                this.toggleRecurringFields();
            });
        },

        setupFieldObserver(field, propertyName) {
            if (!field) return;

            field.addEventListener('change', (event) => {
                this[propertyName] = event.target.value;
            });

            // Optional: Observe for any programmatic changes
            const observer = new MutationObserver((mutations) => {
                mutations.forEach((mutation) => {
                    if (mutation.type === 'attributes' && mutation.attributeName === 'value') {
                        this[propertyName] = field.value;
                    }
                });
            });

            observer.observe(field, {
                attributes: true,
                attributeFilter: ['value']
            });
        },

        toggleRecurringFields() {
            this.recurringFields.forEach(field => {
                try {
                    const fieldName = field.name;
                    
                    let fieldElements = [];
                    let fieldRow;

                    const element = document.getElementById(`id_${fieldName}`);
                    if (element) fieldElements.push(element);
                    fieldRow = element?.closest('.form-row');

                    if (!fieldRow) {
                        console.warn(`Form row for ${fieldName} not found`);
                        return;
                    }

                    const shouldShow = this.type === 'recurring';
                    
                    // Toggle visibility
                    if (shouldShow) {
                        fieldRow.style.display = '';
                        fieldRow.style.opacity = '0';
                        fieldRow.style.maxHeight = '0';
                        fieldRow.classList.remove('hidden');
                        
                        void fieldRow.offsetHeight;
                        
                        fieldRow.style.transition = 'opacity 0.3s, max-height 0.3s';
                        fieldRow.style.opacity = '1';
                        fieldRow.style.maxHeight = '100px';

                        // Make fields required if specified
                        if (field.required) {
                            fieldElements.forEach(element => {
                                element.required = true;
                                
                                // Add visual indicator
                                const label = fieldRow.querySelector('label');
                                if (label && !label.querySelector('.required')) {
                                    const requiredSpan = document.createElement('span');
                                    requiredSpan.className = 'required';
                                    requiredSpan.textContent = '*';
                                    label.appendChild(requiredSpan);
                                }
                            });
                        }
                    } else {
                        fieldRow.style.transition = 'opacity 0.3s, max-height 0.3s';
                        fieldRow.style.opacity = '0';
                        fieldRow.style.maxHeight = '0';
                        
                        setTimeout(() => {
                            fieldRow.classList.add('hidden');
                        }, 300);

                        // Remove required attribute when hidden
                        fieldElements.forEach(element => {
                            element.required = false;
                            
                            // Remove visual indicator
                            const label = fieldRow.querySelector('label');
                            const requiredSpan = label?.querySelector('.required');
                            if (requiredSpan) {
                                requiredSpan.remove();
                            }
                        });
                    }
                } catch (error) {
                    console.error(`Error toggling field ${field.name}:`, error);
                }
            });
        },

        fetchSubcategories(categoryId) {
            this.error = null;
            fetch(`/expenses/get-subcategories/?category_id=${categoryId}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.error) {
                        throw new Error(data.error);
                    }
                    this.subcategories = data;
                    this.updateSubcategoryField();
                })
                .catch(e => {
                    console.error('Error fetching subcategories:', e);
                    this.error = `Failed to load subcategories: ${e.message}`;
                    this.subcategories = [];
                    this.updateSubcategoryField();
                });
        },

        updateSubcategoryField() {
            const subcategoryField = document.getElementById('id_subcategory');
            subcategoryField.innerHTML = '<option value="">---------</option>';
            this.subcategories.forEach(subcategory => {
                const option = document.createElement('option');
                option.value = subcategory.id;
                option.textContent = subcategory.name;
                subcategoryField.appendChild(option);
            });

            if (this.error) {
                const errorDiv = document.createElement('div');
                errorDiv.textContent = this.error;
                errorDiv.style.color = 'red';
                subcategoryField.parentNode.insertBefore(errorDiv, subcategoryField.nextSibling);
            }
        }
    };
}