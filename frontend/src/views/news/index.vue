<template>
  <section>

    <div class="app-container">

        <!-- 搜索区begin -->
       <div class="handle-box">
       <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
            <el-form :inline="true" :model="ff">
                <!----> <el-form-item>
                  博物馆ID： <el-input v-model="ff.museumid"  placeholder="博物馆ID" style="width:200px; heght:30px;" size="mini"></el-input>
                </el-form-item>
                 
                
                <el-form-item>
                   <el-button type="primary" icon="el-icon-search" @click="getResult()" size="mini">搜索</el-button>
                </el-form-item>  

            </el-form>
        </el-col>
         </div>   <!--搜索区end -->

      <!--新增按钮-->
      <div>
        <el-button type="success" icon="el-icon-circle-plus-outline" size="mini" round @click="handleAdd">新增</el-button>
        <!--<el-button type="danger" icon="el-icon-delete" @click="handleDeleteList" size="mini" round>删除</el-button>-->
      </div>

      <!--页面表格显示信息--->
      <template>
        <el-table v-loading="listLoading" :data="list" element-loading-text="Loading" border fit highlight-current-row>

          <el-table-column align="center" label="博物馆ID" width="105">
            <template slot-scope="scope">
              {{ scope.row.fields.museumid }}
            </template>
          </el-table-column>

          <el-table-column label="新闻标题" width="100" align="center">
            <template slot-scope="scope">
              <el-button size="middle" @click="handleSelect(scope.row)">{{ scope.row.fields.newstitle }}</el-button>
            </template>
          </el-table-column>

          <el-table-column label="时间" align="center">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.fields.newstime }}</span>
            </template>
          </el-table-column>

<el-table-column align="center"  label="新闻类别" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.positive_negative }}</span>
            </template>
          </el-table-column>

          <el-table-column label="内容" align="center" width="600">
            <template slot-scope="scope">
              <a href=""> {{ scope.row.fields.newsmaintext }} </a>
            </template>
          </el-table-column>

          

          <el-table-column class-name="status-col" label="Status" width="80" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>

          

          <el-table-column fixed="right" label="操作" align="center">
            <template slot-scope="scope">
              <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="small" @click="handleDeleteList(scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->
    </div>  <!---div class="app-container"结束-->

    <!--新增界面-->
    <el-dialog title="新增博物馆信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="博物馆ID" prop="museumid">
          <el-input v-model="addForm.museumid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="新闻标题" prop="newstitle">
          <el-input v-model="addForm.newstitle" auto-complete="off" />
        </el-form-item>

        <el-form-item label="新闻时间" prop="newstime">
          <el-input v-model="addForm.newstime" auto-complete="off" />
        </el-form-item>

       

        <el-form-item label="新闻类别" prop="positive_negative">
          <el-input v-model="addForm.positive_negative" auto-complete="off" />
        </el-form-item>

     <el-form-item label="新闻内容" prop="newsmaintext">
          <el-input v-model="addForm.newsmaintext" type="textarea" auto-complete="off" />
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
      <el-form ref="selectForm" :inline="true" :model="selectForm" label-width="80px">

        <el-form-item label="博物馆ID" prop="museumid">
          <el-input v-model="selectForm.museumid" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="新闻标题" prop="newstitle">
          <el-input v-model="selectForm.newstitle" type="textarea" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="时间" prop="newstime">
          <el-input v-model="selectForm.newstime" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="性质" prop="positive_negative">
          <el-input v-model="selectForm.positive_negative" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="内容" prop="newsmaintext">
          <el-input v-model="selectForm.newsmaintext" type="textarea" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="status" prop="status">
          <el-input v-model="selectForm.status" auto-complete="off" :disabled="true" />
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="selectFormVisible = false">取消</el-button>
      </div>
    </el-dialog> <!--详细界面结束-->

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form ref="editForm" :inline="true" :model="editForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="博物馆ID" prop="museumid">
          <el-input v-model="editForm.museumid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="新闻标题" prop="newstitle">
          <el-input v-model="editForm.newstitle" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="时间" prop="newstime">
           <el-date-picker  v-model="addForm.newstime" type="date"  placeholder="选择日期" value-format="yyyy-MM-dd"></el-date-picker> 
          <!--el-input v-model="editForm.newstime" auto-complete="off" /-->
        </el-form-item>

        <el-form-item label="性质" prop="positive_negative">
          <el-input v-model="editForm.positive_negative" auto-complete="off" />
        </el-form-item>

        <el-form-item label="内容" prop="newsmaintext">
          <el-input v-model="editForm.newsmaintext" type="textarea" auto-complete="off" />
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
import { getNewsList } from '@/api/table'

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

      ff:{
       museumid: '',
        newsmaintext: '',
        newstime: '',
        newstitle: '',
        positive_negative: '',
        status: ''
      },

      // 新增界面是否显示
      addFormVisible: false,
      // 添加按钮Loading加载
      addLoading: false,
      // 输入框验证
      addFormRules: {
        museumid: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        newstitle: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      // 新增界面数据
      addForm: {
        museumid: '',
        newsmaintext: '',
        newstime: '',
        newstitle: '',
        positive_negative: '',
        status: '1'
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
         museumid: '',
        newsmaintext: '',
        newstime: '',
        newstitle: '',
        positive_negative: '',
        
        status: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      addFormRules: {
        museumid: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        newstitle: [{ required: true, message: '请输入新闻标题', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      editForm: {
         museumid: '',
        newsmaintext: '',
        newstime: '',
        newstitle: '',
        positive_negative: '',
        status: ''
      }
    }// end return
  },

  created() {
    this.fetchData()
  },
  methods: {

    getResult: function() {
      var _this = this;
      this.listLoading = true;
      let param = Object.assign(
        {},
        {
          museumid: this.ff.museumid,
        }
      );
      this.$ajax({
        method: "get",
        url: "news",
        data: param
      }).then(function(response) {
        _this.ff = response.data.items.fields;
        _this.listLoading = false;
      });
    },

    fetchData() {
      this.listLoading = true
      getNewsList().then(response => {
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
