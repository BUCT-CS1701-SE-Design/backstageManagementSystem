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
          
          <el-table-column align="center" label="ID" width="55">
            <template slot-scope="scope">
              {{ scope.$index }}
            </template>
          </el-table-column>
          <el-table-column align="center" label="藏品ID" width="75">
            <template slot-scope="scope">
              {{ scope.row.pk }}
            </template>
          </el-table-column>

          <el-table-column label="藏品名称" width="220" align="center">
            <template slot-scope="scope">

              <el-button size="middle" @click="handleSelect(scope.row)">{{ scope.row.fields.collectionname }}</el-button>

            </template>

          </el-table-column>

          <el-table-column label="藏品介绍" align="center" width="550">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.collectionintroduction }}</span>
            </template>
          </el-table-column>
          <el-table-column label="藏品年代" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.collection_age }}</span>
            </template>
          </el-table-column>

          <el-table-column label="图片链接" align="center" width="200">
            <template slot-scope="scope">
              <a href=""> {{ scope.row.fields.collectionimage }} </a>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="Status" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column align="center" prop="created_at" label="所属博物馆ID">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.museumid }}</span>
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
    <el-dialog title="新增藏品信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="所属博物馆ID" prop="museumid">
          <el-input v-model="addForm.museumID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品ID" prop="collectionid">
          <el-input v-model="addForm.CollectionID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品名称" prop="collectionname">
          <el-input v-model="addForm.collectionName" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品介绍"  prop="collectionintroduction">
          <el-input v-model="addForm.collectionintroduction" type="textarea" auto-complete="off" />
        </el-form-item>



        <el-form-item label="藏品年代" prop="collection_age">
          <el-input v-model="addForm.collection_age" auto-complete="off" />
        </el-form-item>

        <el-form-item label="图片链接" prop="collectionimage">
          <el-input v-model="addForm.collectionimage" auto-complete="off" />
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

        <el-form-item label="所属博物馆ID" prop="museumid" >
          <el-input v-model="selectForm.museumid" auto-complete="off" :disabled="true" />
        </el-form-item>

       <!-- <el-form-item label="藏品ID" prop="CollectionID">
          <el-input v-model="selectForm.CollectionID" auto-complete="off" :disabled="true" />
        </el-form-item> -->

        <el-form-item label="藏品名称" prop="collectionname">
          <el-input v-model="selectForm.collectionname" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="藏品介绍" prop="collectionintroduction">
          <el-input v-model="selectForm.collectionintroduction" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="藏品年代" prop="collection_age">
          <el-input v-model="selectForm.collection_age" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="图片链接" prop="collectionimage">
          <el-input v-model="selectForm.collectionimage" auto-complete="off" :disabled="true" />
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

        <el-form-item label="藏品名称" prop="collectionname">
          <el-input v-model="editForm.collectionname" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品介绍" prop="collectionintroduction">
          <el-input v-model="editForm.collectionintroduction" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品年代" prop="collection_age">
          <el-input v-model="editForm.collection_age" auto-complete="off" />
        </el-form-item>

        <el-form-item label="图片链接" prop="collectionimage">
          <el-input v-model="editForm.collectionimage" auto-complete="off" />
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
        museumid: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        collectionid: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      // 新增界面数据
      addForm: {
         museumid: '',
        collectionid: '',
        collectionname: '',
        collectionintroduction: '',
        collection_age: '',
        collectionimage: '',
        status: '1'
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
        museumid: '',
        //CollectionID: '',
        collectionname: '',
        collectionintroduction: '',
        collection_age: '',
        collectionimage: '',
        status: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      addFormRules: {
        museumid: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        collectionid: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      editForm: {
         museumid: '',
        collectionid: '',
        collectionname: '',
        collectionintroduction: '',
        collection_age: '',
        collectionimage: '',
        status: '1'
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
