<template>
    <div class="overflow-auto">
        <b-pagination
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
        ></b-pagination>
        <b-table ref="table" hover :per-page="perPage"
                 :current-page="currentPage"
                 small :items="items" :fields="fields"></b-table>
    </div>
</template>

<script>
    export default {
        components:{

        },

        data(){
            return{
                perPage: 3,
                currentPage: 1,
                name: "Gauge",
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

        computed: {
            rows() {
                return this.items.length
            }
        },

        methods:{
            updateTable: function (data) {
                if (data != null) {
                    this.items = data;
                    this.$refs.table.refresh();
                }
            }
        }
    }
</script>

<style scoped>

</style>