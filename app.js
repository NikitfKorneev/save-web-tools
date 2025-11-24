// Создаем Vue приложение
const { createApp } = Vue;

createApp({
    // DATA - реактивные данные
    data() {
        return {
            // 1. Интерполяция
            userName: 'Пользователь',
            userAge: 25,
            
            // 2. Условный рендеринг
            isVisible: true,
            
            // 3. Списки
            items: ['Элемент 1', 'Элемент 2', 'Элемент 3'],
            newItem: '',
            
            // 4. События
            clickCount: 0,
            
            // 5. Вычисляемые свойства
            price: 100,
            quantity: 1,
            
            // 6. Классы и стили
            isActive: false,
            hasError: false,
            boxColor: '#ecf0f1',
            
            // 7. Watchers
            counter: 0,
            previousCounter: 0
        }
    },

    // COMPUTED - вычисляемые свойства (кэшируются)
    computed: {
        totalPrice() {
            return this.price * this.quantity;
        }
    },

    // METHODS - методы
    methods: {
        // 2. Условный рендеринг
        toggleVisibility() {
            this.isVisible = !this.isVisible;
        },

        // 3. Работа со списками
        addItem() {
            if (this.newItem.trim()) {
                this.items.push(this.newItem.trim());
                this.newItem = '';
            }
        },

        removeItem(index) {
            this.items.splice(index, 1);
        },

        // 4. Обработка событий
        incrementCounter() {
            this.clickCount++;
        },

        resetCounter() {
            this.clickCount = 0;
        },

        // 5. Методы для количества
        increaseQuantity() {
            this.quantity++;
        },

        decreaseQuantity() {
            if (this.quantity > 1) {
                this.quantity--;
            }
        },

        // 6. Работа с классами
        toggleBox() {
            this.isActive = !this.isActive;
            this.hasError = !this.hasError;
        }
    },

    // WATCHERS - наблюдатели
    watch: {
        counter(newValue, oldValue) {
            this.previousCounter = oldValue;
            console.log(`Счетчик изменился с ${oldValue} на ${newValue}`);
        },

        userName(newName) {
            console.log(`Имя пользователя изменено на: ${newName}`);
        }
    },

    // LIFECYCLE HOOKS - хуки жизненного цикла
    mounted() {
        console.log('Компонент примонтирован к DOM');
    },

    updated() {
        console.log('Компонент обновлен');
    }
}).mount('#app');