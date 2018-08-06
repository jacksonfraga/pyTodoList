var app = new Vue({
    el: '#app',
    data: {
        cloneTodos : [],
        todos : [
        ],
        todo: ''
    },
    methods: {
        addTodo: function() {
            data = { description : this.todo }
            this.$http.post('/api/todo/', data).then(response => {
                this.todos.push(response.body)
                this.todo = ''
            }, response => {
                alert('erro ao gravar')
            });
        },
        deleteTodo: function(todo) {
            alert('/api/todo/'.concat(todo.todo_id))
            this.$http.delete('/api/todo/'.concat(todo.todo_id)).then(response => {
                if (response.body.success) {
                    this.todos.splice(this.todos.indexOf(todo), 1)
                }
            }, response => {
                // error callback
            });
        },
        onlyDone: function() {
            this.$http.get('/api/todo/done').then(response => {
                // get body data
                this.todos = response.body.todos
            }, response => {
                // error callback
            });
        },
        onlyDoing: function() {
            this.$http.get('/api/todo/doing').then(response => {
                // get body data
                this.todos = response.body.todos
            }, response => {
                // error callback
            });
        },
        listAll: function() {
            this.$http.get('/api/todo/all').then(response => {
                // get body data
                this.todos = response.body.todos
            }, response => {
                // error callback
            });
        },
        addTodoOld: function() {
            var value = this.todo && this.todo.trim()
            if (!value) return;
            this.todos.push({ description: value, done: 0 })
            this.todo = ''
        }
    },
    mounted: function(){
        this.listAll()
    },
    created (){
        var vm = this;
        this.$watch("todos", function (after, before) {
            after.filter( function( p, idx ) {
                return Object.keys(p).some( function( prop ) {
                    var diff = p[prop] !== vm.cloneTodos[idx][prop];
                    if(diff) {
                        p.changed = true;
                        vm.cloneTodos[idx][prop] = p[prop];
                    }
                })
            });

        }, {deep: true})
    }
})