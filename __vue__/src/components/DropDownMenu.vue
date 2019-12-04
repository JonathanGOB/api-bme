<template>
    <div>
        <b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>
        <div class="mt-3">u have selected: <strong>{{ selected }}</strong></div>
    </div>
</template>

<script>
    export default {
        name: "DropDownMenu",
        data(){
            return{
                selected: null,
                options:[
                    {value: null, text: 'select'},
                    {value: 'ESP1', text: 'ESP1'},
                    {value: 'ESP2', text: 'ESP1'}
                ]
            }
        }
    }
</script>

<style scoped>

</style>