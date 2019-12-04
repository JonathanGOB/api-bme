<template>
    <div>
        <b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>
        <div class="mt-3">u have selected: <strong>{{ selected }}</strong></div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "DropDownMenu",
        data(){
            return{
                posts: [],
                selected: null,
                options:[
                    {value: null, text: 'select'},
                    {value: 'ESP1', text: 'ESP1'},
                    {value: 'ESP2', text: 'ESP1'}
                ]
            }
        },
        created() {
            axios.get(`http://jsonplaceholder.typicode.com/posts`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.posts = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
        }
    }
</script>

<style scoped>

</style>