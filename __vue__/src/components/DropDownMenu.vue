<template>
    <div>
        <b-form-select @change="sendSelected(selected)" v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>
        <div class="mt-3">u have selected: <strong>{{ selected }}</strong></div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "DropDownMenu",
        data(){
            return{
                options: [
                    {value: null, text: 'select sensor'},
                    {value: 'all', text: 'all'}
                ],
                selected: null,
            }
        },
        methods:{
            sendSelected: function(selected){
                this.$emit('selected', selected)
            },
            
            getOptions: function(){
                axios.get(`http://127.0.0.1:5000/Api/V1/Devices`)
                    .then(response => {
                        // JSON responses are automatically parsed.
                        response.data.Data.forEach(deviceName => this.options.push({value : deviceName['device_id'], text: deviceName['device_id']}));
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