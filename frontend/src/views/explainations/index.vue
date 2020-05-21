<template>
  <section>

    <div class="app-container">

      <!--新增按钮-->
      <div>
        <el-button type="success" icon="el-icon-circle-plus-outline" size="mini" round @click="handleAdd">新增</el-button>
        <!--<el-button type="danger" icon="el-icon-delete" @click="handleDeleteList" size="mini" round>删除</el-button>-->
      </div>

      <!--页面表格显示信息--->
      <template>
        <el-table v-loading="listLoading" :data="list" element-loading-text="Loading" border fit highlight-current-row>

          <!--索引-->
          <el-table-column type="index" :index="indexMethod" />

          <el-table-column align="center" label="ID" width="75">
            <template slot-scope="scope">
              {{ scope.row.pk }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="讲解ID" width="75">
            <template slot-scope="scope">
              {{ scope.row.fields.explanationID }}
            </template>
          </el-table-column>

          <el-table-column label="讲解名称" width="100" align="center">
            <template slot-scope="scope">
              <el-button size="middle" @click="handleSelect(scope.$index,scope.row)">{{ scope.row.fields.explanationName }}</el-button>
            </template>
          </el-table-column>

          <el-table-column label="讲解人ID" align="center" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.explainerID }}</span>
            </template>
          </el-table-column>

          <el-table-column label="讲解时间" align="center" width="100">
            <template slot-scope="scope">
              {{ scope.row.fields.explanationTime }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="讲解语言" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.explanationLanguage }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="推荐时间" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.recommendedTime }}</span>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="Status" width="80" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column fixed="right" label="操作" align="center" width="200">
            <template slot-scope="scope">
              <el-button size="small" @click="handleEdit(scope.$index,scope.row)">编辑</el-button>
              <el-button size="small" @click="handleDeleteList(scoped.$index,scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->

      <!-- 分页 -->
      <el-pagination :current-page="currentPage" :page-size="pageSize" layout="total, prev, pager, next" :total="count" @current-change="getResult" />
    </div>  <!---div class="app-container"结束-->

    <!--新增界面-->
    <el-dialog title="新增讲解信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="讲解ID" prop="explanationID">
          <el-input v-model="addForm.explanationID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解名称" prop="explanationName">
          <el-input v-model="addForm.explanationName" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解人ID" prop="explainerID">
          <el-input v-model="addForm.explainerID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览时间" prop="explanationTime">
          <el-input v-model="addForm.explanationTime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解语言" prop="explanationLanguage">
          <el-input v-model="addForm.explanationLanguage" auto-complete="off" />
        </el-form-item>

        <el-form-item label="推荐时间" prop="recommendedTime">
          <el-input v-model="addForm.recommendedTime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="status" prop="status">
          <el-input v-model="addForm.status" auto-complete="off" />
        </el-form-item>

      </el-form>

      <!--提交或者取消-->
      <div slot="footer" class="dialog-footer">
        <el-button @click="addFormVisible = false">取消</el-button>
        <!--<el-button type="primary" @click="addSubmit" :loading="addLoading">提交</el-button>
        -->
      </div>
    </el-dialog>
    <!--新增界面结束-->

    <!--详细界面-->
    <el-dialog title="详细信息" :visible.sync="selectFormVisible" :close-on-click-modal="false">

        <el-card>
      
  <div   class="text item">
     {{"讲解ID: "+selectForm.explanationID}}
     <br><br>
    {{"讲解内容:  "+selectForm.explanationName}}
      <br><br>
      {{"讲解人ID： "+selectForm.explainerID}}
       <br><br>
       {{"讲解时间： "+selectForm.explanationTime}}
        <br><br>
        {{"讲解语言： "+selectForm.explanationLanguage}}
        <br><br>
        {{"推荐时间: "+selectForm.recommendedTime}}
         <br><br>
         {{"status: "+selectForm.status}}
  </div>
</el-card>

    </el-dialog> <!--详细界面结束-->

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form ref="editForm" :inline="true" :model="editForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="讲解ID" prop="explanationID">
          <el-input v-model="editForm.explanationID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解名称" prop="explanationName">
          <el-input v-model="editForm.explanationName" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解人ID" prop="explainerID">
          <el-input v-model="editForm.explainerID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解时间" prop="explanationTime">
          <el-input v-model="editForm.explanationTime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="讲解语言" prop="explanationLanguage">
          <el-input v-model="editForm.explanationLanguage" auto-complete="off" />
        </el-form-item>

        <el-form-item label="推荐时间" prop="recommendedTime">
          <el-input v-model="editForm.recommendedTime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="status" prop="status">
          <el-input v-model="editForm.status" auto-complete="off" />
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editFormVisible = false">取消</el-button>
        <!--	<el-button type="primary" @click="editSubmit" :loading="editLoading">提交</el-button>-->
      </div>
    </el-dialog><!--编辑界面结束-->

  </section>
</template>


<script>
import { getexplainationsList } from '@/api/table'

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

      // 分页
      count: 0,
      currentPage: 1,
      pageSize: 10,

      // 新增界面是否显示
      addFormVisible: false,
      // 添加按钮Loading加载
      addLoading: false,
      // 输入框验证
      addFormRules: {
        // museumID: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        // museumname: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      // 新增界面数据
      addForm: {
        explanationID: '',
        explanationName: '',
        explainerID: '',
        explanationTime: '',
        explanationLanguage: '',
        recommendedTime: '',
        status: ''
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
        explanationID: '',
        explanationName: '',
        explainerID: '',
        explanationTime: '',
        explanationLanguage: '',
        recommendedTime: '',
        status: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      // addFormRules: {
      //  museumID: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
      //  museumname: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
      //  status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      // },
      editForm: {
        explanationID: '',
        explanationName: '',
        explainerID: '',
        explanationTime: '',
        explanationLanguage: '',
        recommendedTime: '',
        status: ''
      }
    }// end return
  },

  created() {
    this.fetchData()
  },
  methods: {

    // table序号
    indexMethod(index) {
      return index + 1
    },

    getResult: function(val) {
      var _this = this
      this.listLoading = true
      const param = Object.assign(
        {},
        {
          currentPage: val,
          pageSize: 10,
          userName: this.filters.userName,
          userNo: this.filters.userNo,
          job: this.filters.job,
          loginName: this.filters.loginName,
          mobile: this.filters.mobile,
          sex: this.filters.sex
        }
      )
      this.$ajax({
        method: 'post',
        url: 'test',
        data: param
      }).then(function(resultData) {
        _this.tableData = resultData.data.data
        _this.count = resultData.data.count
        _this.listLoading = false
      })
    },


    fetchData() {
      this.listLoading = true
      getexplainationsList().then(response => {
        this.list = response.data.items
        console.log(response.data.items.fields)
        this.listLoading = false
      })
    },

    // 显示新增界面
    handleAdd: function() {
      this.addFormVisible = true
    },
    // 新增
    addSubmit: function() {
      this.$refs.addForm.validate(valid => {
        if (valid) {
          // 如果性别未选择给默认值
          // if (this.addForm.sex == "") {
          //   this.addForm.sex = "-1";
          // }

          this.$confirm('确认提交吗？', '提示', {}).then(() => {
            this.addLoading = true
            const param = Object.assign({}, this.addForm)
            console.log(param)
            this.$ajax({
              method: 'post',
              url: 'museumadd',
              data: param
            }).then(res => {
              this.addLoading = false
              this.$message({
                message: '提交成功',
                type: 'success'
              })
              this.$refs['addForm'].resetFields()
              this.addFormVisible = false
              this.fetchData()
            })
          })
        }// end if
      })
    },

    // 查看详细信息
    handleSelect: function(index, row) {
      this.selectFormVisible = true
      this.selectForm = Object.assign({}, row.fields)
    },

    // 显示编辑界面
    handleEdit: function(index, row) {
      this.editFormVisible = true
      this.editForm = Object.assign({}, row.fields)
    },
    // 编辑
    editSubmit: function() {
      this.$refs.editForm.validate(valid => {
        if (valid) {
          this.$confirm('确认提交吗？', '提示', {}).then(() => {
            this.editLoading = true
            const param = Object.assign({}, this.editForm)
            console.log(param)
            this.$ajax({
              method: 'post',
              url: '/api/sysuser-api/addUser',
              data: param
            }).then(res => {
              this.editLoading = false
              this.$message({
                message: '提交成功',
                type: 'success'
              })
              this.$refs['editForm'].resetFields()
              this.editFormVisible = false
              this.getResult(1)
            })
          })
        }
      })
    },

    // 删除
    handleDeleteList: function(index, row) {
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
      /*
        .then(() => {
          this.listLoading = true;
          let param = new URLSearchParams();
          param.append("ids", id);
          console.log("ids:" + param);
          this.$ajax({
            method: "post",
            url: "/api/sysuser-api/delSysUserByUserId",
            data: param
          }).then(res => {
            this.listLoading = false;
            this.$message({
              message: "删除成功",
              type: "success"
            });
            this.selectList = [];
            this.getResult(1);
          });
        })
        .catch(() => {});*/
    }

  }
}
</script>
