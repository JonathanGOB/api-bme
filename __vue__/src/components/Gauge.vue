<template>
    <div class="overflow-auto" >
        <b-pagination style="margin-top: 25px"
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
                pills class="mt-4"
                      :limit="3"

        >
            <template v-slot:ellipsis-text>
                <b-spinner small type="grow"></b-spinner>
            </template>
            <template v-slot:page="{ page, active }">
                <b v-if="active">{{ page }}</b>
                <i v-else>{{ page }}</i>
            </template>
        </b-pagination>

        <b-table ref="table" hover :per-page="perPage"
                 :current-page="currentPage"
                 small :items="items" :fields="fields"></b-table>
    </div>
</template>

<script>
    export default {
        components: {},

        data() {
            return {
                perPage: 3,
                currentPage: 1,
                name: "Gauge",
                items: [],
                fields: [
                    {key: 'id_num', label: 'id_num', sortable: true},
                    {key: 'device_id', label: 'device_id', sortable: true},
                    {key: 'pressure', label: 'pressure', sortable: true},
                    {key: 'temperature', label: ' temperature', sortable: true},
                    {key: 'humidity', label: 'humidity', sortable: true},
                    {key: 'timestamp', label: 'timestamp', sortable: true},
                    {key: 'uri', label: 'uri', sortable: false},
                ],
            }
        },

        computed: {
            rows() {
                return this.items.length
            }
        },

        methods: {
            updateTable: function (data) {
                if (data != null) {
                    //sorts data
                    let methodData = data.data.Data.sort(function (a, b) {
                        return new Date(a.timestamp) - new Date(b.timestamp);
                    });
                    this.items = methodData;
                    this.$refs.table.refresh();
                }
            }
        }
    }
</script>

<style scoped>

</style>