function expenseForm() {
    return {
        category: null,
        subcategories: [],
        error: null,
        
        init() {
            this.$watch('category', value => {
                if (value) {
                    this.fetchSubcategories(value);
                } else {
                    this.subcategories = [];
                    this.updateSubcategoryField();
                }
            });

            this.category = document.getElementById('id_category').value;
            if (this.category) {
                this.fetchSubcategories(this.category);
            }
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