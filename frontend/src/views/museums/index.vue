<template>

  <div class="app-container">
    <div>
      <p>博物馆信息 </p>
    </div>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.row.pk }}
        </template>
      </el-table-column>
      <el-table-column label="博物馆名">
        <template slot-scope="scope">
          {{ scope.row.fields.museumname }}
        </template>
      </el-table-column>
      <el-table-column label="地址" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.fields.location }}</span>
        </template>
      </el-table-column>
      <el-table-column label="官网链接" align="center">
        <template slot-scope="scope">
          <a href=""> {{ scope.row.fields.link }} </a>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        active: 1,
        deleted: 0
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      fields: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        this.fields = this.list.fields
        console.log(response.data.items)
        this.listLoading = false
      })
    }
  }
}
</script>
