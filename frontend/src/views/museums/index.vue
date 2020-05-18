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
      <el-table-column label="博物馆名" width="100">
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
          <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="开放时间" width="400">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.fields.opentime }}</span>
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
        1: 'success',
        0: 'gray'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      fieldds: null,
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
        console.log(response.data.items.fields)
        this.listLoading = false
      })
    }
  }
}
</script>
