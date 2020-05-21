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
          <el-table-column align="center" label="数据ID" type="index" :index="indexMethod" width="70" />

          <el-table-column align="center" label="用户ID" width="150">
            <template slot-scope="scope">
              {{ scope.row.fields.idcard }}
            </template>
          </el-table-column>

          <el-table-column label="用户名" width="220" align="center">
            <template slot-scope="scope">
              <el-button size="middle" @click="handleSelect(scope.row)">{{ scope.row.fields.username }}</el-button>
            </template>
          </el-table-column>

          <el-table-column label="用户昵称" align="center" width="150">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.nickname }}</span>
            </template>
          </el-table-column>

          <el-table-column label="密码" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.password}}</span>
            </template>
          </el-table-column>

          <el-table-column label="联系方式" align="center" width="150">
            <template slot-scope="scope">
               {{ scope.row.fields.telephone }} 
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="用户创建时间" width="150" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.usercreatedate }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center"  label="用户角色">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.userrole }}</span>
            </template>
          </el-table-column>

          <el-table-column fixed="right" label="操作" align="center"  width="200">
            <template slot-scope="scope">
              <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="small" @click="handleDeleteList(scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->
    </div>  <!---div class="app-container"结束-->

    <!--新增界面-->
    <el-dialog title="新增用户" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="用户ID" prop="idcard">
          <el-input v-model="addForm.idcard" auto-complete="off" />
        </el-form-item>

        <el-form-item label="用户名" prop="username">
          <el-input v-model="addForm.username" auto-complete="off" />
        </el-form-item>

        <el-form-item label="用户昵称" prop="nickname">
          <el-input v-model="addForm.nickname" auto-complete="off" />
        </el-form-item>

        <el-form-item label="密码"  prop="password">
          <el-input v-model="addForm.password"  auto-complete="off" />
        </el-form-item>



        <el-form-item label="角色" prop="userrole">
          <el-input v-model="addForm.userrole" auto-complete="off" />
        </el-form-item>

        <!--<el-form-item label="创建时间" prop="usercreatedate">
          
          <el-input v-model="addForm.usercreatedate" auto-complete="off" :disabled="true"/>
        </el-form-item>-->

      </el-form>

      <!--提交或者取消-->
      <div slot="footer" class="dialog-footer">
        <el-button @click="addFormVisible = false">取消</el-button>
        <el-button type="primary" @click="addSubmit" :loading="addLoading">提交</el-button>
      
      </div>
    </el-dialog>
    <!--新增界面结束-->

    <!--详细界面-->
    <el-dialog title="详细信息" :visible.sync="selectFormVisible" :close-on-click-modal="false">
      <el-form ref="selectForm" :inline="true" :model="selectForm" label-width="80px">

        <el-form-item label="用户ID" prop="idcard" >
          <el-input v-model="selectForm.idcard" auto-complete="off" :disabled="true" />
        </el-form-item>

       

        <el-form-item label="用户名" prop="username">
          <el-input v-model="selectForm.username" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="用户昵称" prop="nickname">
          <el-input v-model="selectForm.nickname" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="密码"  prop="password">
          <el-input v-model="selectForm.password"  auto-complete="off" :disabled="true" />
        </el-form-item>



        <el-form-item label="角色" prop="userrole">
          <el-input v-model="selectForm.userrole" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="创建时间" prop="usercreatedate">
          
          <el-input v-model="selectForm.usercreatedate" auto-complete="off" :disabled="true"  />
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="selectFormVisible = false">取消</el-button>
      </div>
    </el-dialog> <!--详细界面结束-->

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form ref="editForm" :inline="true" :model="editForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="用户ID" prop="idcard">
          <el-input v-model="editForm.idcard" auto-complete="off" />
        </el-form-item>

        <el-form-item label="用户名" prop="username">
          <el-input v-model="editForm.username" auto-complete="off" />
        </el-form-item>

        <el-form-item label="用户昵称" prop="nickname">
          <el-input v-model="editForm.nickname" auto-complete="off" />
        </el-form-item>

        <el-form-item label="密码"  prop="password">
          <el-input v-model="editForm.password"  auto-complete="off" />
        </el-form-item>



        <el-form-item label="角色" prop="userrole">
          <el-input v-model="editForm.userrole" auto-complete="off" />
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editFormVisible = false">取消</el-button>
        	<el-button type="primary" @click="editSubmit" :loading="editLoading">提交</el-button>
      </div>
    </el-dialog><!--编辑界面结束-->

  </section>
</template>

<script>
import { getuserList } from '@/api/table'

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

      // 新增界面是否显示
      addFormVisible: false,
      // 添加按钮Loading加载
      addLoading: false,
      // 输入框验证
      addFormRules: {
        idcard: [{ required: true, message: '请输入用户ID', trigger: 'blur' }],
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入用户密码', trigger: 'blur' }],
        userrole: [{ required: true, message: '请输入用户角色', trigger: 'blur' }],
        usercreatedate: [{ required: true, message: '请输入用户是否可以创建数据', trigger: 'blur' }]
      },
      // 新增界面数据
      

      addForm: {
        idcard: '',
        nickname: '',
        password: '',
        telephone: '',
       // usercreatedate: "",
        username: '',
        userrole: ''
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
       idcard: '',
        nickname: '',
        password: '',
        telephone: '',
        usercreatedate: '',
        username: '',
        userrole: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      addFormRules: {
        idcard: [{ required: true, message: '请输入用户ID', trigger: 'blur' }],
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入用户密码', trigger: 'blur' }],
        userrole: [{ required: true, message: '请输入用户角色', trigger: 'blur' }],
        usercreatedate: [{ required: true, message: '请输入用户是否可以创建数据', trigger: 'blur' }]
      },
      editForm: {
          idcard: '',
        nickname: '',
        password: '',
        telephone: '',
      //  usercreatedate: '',
        username: '',
        userrole: ''
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

    fetchData() {
      this.listLoading = true
      getuserList().then(response => {
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
    handleSelect: function(row) {
      this.selectFormVisible = true
      this.selectForm = Object.assign({}, row.fields)
    },

    // 显示编辑界面
    handleEdit: function(row) {
      this.editFormVisible = true
      this.editForm = Object.assign({}, row.fields)
    },
    // 编辑
    editSubmit: function() {
      if (this.checked == true) {
        this.editForm.isLocked = '1'
      }
      if (this.checked == false) {
        this.editForm.isLocked = '0'
      }
      // 主机构必填提示
      if (this.editForm.orgid == '') {
        this.$message({
          message: '请选择主机构',
          type: 'error'
        })
        return
      }
      // 岗位必填提示
      if (this.editForm.positionid == '') {
        this.$message({
          message: '请选择岗位',
          type: 'error'
        })
        return
      }
      // 如果性别未选择给默认值
      if (this.editForm.sex == '') {
        this.editForm.sex = '-1'
      }
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
