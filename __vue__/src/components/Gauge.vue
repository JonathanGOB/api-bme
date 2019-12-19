<template>
    <b-table ref="table" hover :items="items" :fields="fields"></b-table>
</template>

<script>
    export default {
        name: "Gauge",
        components:{

        },

        data(){
            return{
                items: [],
                fields: [
                    { key: 'id_num', label: 'id_num', sortable: true},
                    { key: 'device_id', label: 'device_id', sortable: true},
                    { key: 'pressure', label: 'pressure', sortable: true},
                    { key: ' temperature', label: ' temperature', sortable: true},
                    { key: 'humidity', label: 'humidity', sortable: true},
                    { key: 'timestamp', label: 'timestamp', sortable: true},
                    { key: 'uri', label: 'uri', sortable: false},
                ],
            }
        },

        methods:{
            updateTable: function (data) {
                if (data != null) {
                    // eslint-disable-next-line no-console
                    console.log("data gauge: ", data);
                    this.items = data;
                    this.$refs.table.refresh();
                    // eslint-disable-next-line no-console
                    console.log("items gauge: ",  this.items);
                }
            }
        }
    }
</script>

<style scoped>

</style>