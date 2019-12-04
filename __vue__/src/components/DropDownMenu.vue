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
                options: [],
                selected: null,
            }
        },
        methods:{
            getOptions: function(){
                axios.get(`http://127.0.0.1:5000/Api/V1/Devices`)
                    .then(response => {
                        // JSON responses are automatically parsed.
                        response.data.Data.forEach(deviceName => this.options.push(deviceName['device_id']));
                    })
                    .catch(e => {
                        this.errors.push(e)
                    })
            }
        },

        beforeMount(){
            this.getOptions();
        }
    }
</script>

<style scoped>

</style>