<template>
  <section>

    <div class="app-container">

      

      <!--页面表格显示信息--->
      <template>
        <el-table v-loading="listLoading" :data="list" element-loading-text="Loading" border fit highlight-current-row>
          <el-table-column align="center" label="ID" width="55">
            <template slot-scope="scope">
              {{ scope.$index }}
            </template>
          </el-table-column>
          <el-table-column align="center" label="ID" width="95">
            <template slot-scope="scope">
              {{ scope.$index }}
            </template>
          </el-table-column>
          <el-table-column label="评论内容">
            <template slot-scope="scope">
              {{ scope.row.fields.comment }}
            </template>
          </el-table-column>
          <el-table-column label="评论者ID" width="110" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.userid }}</span>
            </template>
          </el-table-column>
          <el-table-column label="环境评分" width="50" align="center">
            <template slot-scope="scope">
              {{ scope.row.fields.sentianalysis_environment }}
            </template>
          </el-table-column>
          <el-table-column label="展览评分" width="50" align="center">
            <template slot-scope="scope">
              {{ scope.row.fields.sentianalysis_exhibit }}
            </template>
          </el-table-column>
          <el-table-column label="服务评分" width="50" align="center">
            <template slot-scope="scope">
              {{ scope.row.fields.sentianalysis_service }}
            </template>
          </el-table-column>
          <el-table-column class-name="status-col" label="Status" width="110" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column align="center" prop="created_at" label="评论时间" width="200">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.fields.commentdate }}</span>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="操作" align="center">
            <template slot-scope="scope">
              <el-button size="small" @click="handleDeleteList(scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->
    </div>  <!---div class="app-container"结束-->

  </section>
</template>

<script>
import { getCommentList } from '@/api/table'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        1: 'success',
        0: 'delete'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true,
    }
    },

     
    

  created() {
    this.fetchData()
  },
  methods: {

    fetchData() {
      this.listLoading = true
      getCommentList().then(response => {
        this.list = response.data.items
        this.listLoading = false
      })
    },

    // 删除
    handleDeleteList: function(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      })
        .then(() => {
          row.fields.status = 0
          this.$message({
            message: '删除成功',
            type: 'success'
          })
        }
        )
    }
  }

}
</script>