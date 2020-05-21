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

          <el-table-column label=" 展览主题 " width="200" align="center">
            <template slot-scope="scope">

              <el-button size="middle" @click="handleSelect(scope.$index,scope.row)">{{ scope.row.fields.exhibitiontheme }}</el-button>

            </template>

          </el-table-column>

          <el-table-column label="展览介绍" align="center" width="300">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.exhibitionintroduction }}</span>
            </template>
          </el-table-column>

          <el-table-column label="展览时间" align="center">
            <template slot-scope="scope">
              {{ scope.row.fields.exhibitionTime }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="展览位置">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.exhibitionLocation }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="展览电话" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.exhibitionTel }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="展览事件" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.exhibitionThingList }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="展览图片" width="200">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.exhibition_picture }}</span>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="Status" width="80" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column fixed="right" label="操作" align="center" width="100">
            <template slot-scope="scope">
              <el-button size="small" @click="handleEdit(scope.$index,scope.row)">编辑</el-button>
              <el-button size="small" @click="handleDeleteList(scope.$index,scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->
    </div>  <!---div class="app-container"结束-->

    <!--新增界面-->
    <el-dialog title="新增展览信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="博物馆ID" prop="museumid">
          <el-input v-model="addForm.museumid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览ID" prop="exhibitionid">
          <el-input v-model="addForm.exhibitionid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览时间" prop="exhibitiontime">
          <el-input v-model="addForm.exhibitiontime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览主题" prop="exhibitiontheme">
          <el-input v-model="addForm.exhibitiontheme" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览介绍" prop="exhibitionIntroduction">
          <el-input v-model="addForm.exhibitionIntroduction" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览位置" prop="exhibitionlocation">
          <el-input v-model="addForm.exhibitionlocation" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览事件" prop="exhibitionthingList">
          <el-input v-model="addForm.exhibitionthinglist" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览图片" prop="exhibition_picture">
          <el-input v-model="addForm.exhibition_picture" auto-complete="off" />
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

        <el-form-item label="展览ID" prop="exhibitionid">
          <el-input v-model="selectForm.exhibitionid" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览时间" prop="exhibitiontime">
          <el-input v-model="selectForm.exhibitiontime" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览主题" prop="exhibitiontheme">
          <el-input v-model="selectForm.exhibitiontheme" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览介绍" prop="exhibitionintroduction">
          <el-input v-model="selectForm.exhibitionintroduction" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览位置" prop="exhibitionlocation">
          <el-input v-model="selectForm.exhibitionlocation" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览电话" prop="exhibitiontel">
          <el-input v-model="selectForm.exhibitiontel" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览事件" prop="exhibitionthinglist">
          <el-input v-model="selectForm.exhibitionthinglist" auto-complete="off" :disabled="true" />
        </el-form-item>

        <el-form-item label="展览图片" prop="exhibition_picture">
          <el-input v-model="selectForm.exhibition_picture" auto-complete="off" :disabled="true" />
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
          <el-input v-model="editForm.museumID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览ID" prop="exhibitionid">
          <el-input v-model="editForm.exhibitionid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览时间" prop="exhibitiontime">
          <el-input v-model="editForm.exhibitiontime" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览主题" prop="exhibitiontheme">
          <el-input v-model="editForm.exhibitiontheme" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览介绍" prop="exhibitionintroduction">
          <el-input v-model="editForm.exhibitionintroduction" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览位置" prop="exhibitionlocation">
          <el-input v-model="editForm.exhibitionlocation" auto-complete="off" />
        </el-form-item>

        <el-form-item label="展览电话" prop="exhibitiontel">
          <el-input v-model="editForm.exhibitiontel" auto-complete="off" />
        </el-form-item>


        <el-form-item label="展览事件" prop="exhibitionthinglist">
          <el-input v-model="editForm.exhibitionthinglist" auto-complete="off" />
        </el-form-item>

        <el-form-item label="图片链接" prop="exhibition_picture">
          <el-input v-model="editForm.exhibition_picture" type="textarea" auto-complete="off" />
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
import { getExhibitionList } from '@/api/table'

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
        exhibitionid: [{ required: true, message: '请输入展览ID', trigger: 'blur' }],
        exhibitiontheme: [{ required: true, message: '请输入展览主题', trigger: 'blur' }],
        status: [{ required: true, message: '请输入状态', trigger: 'blur' }]
      },
      // 新增界面数据
      addForm: {
        museumid: '',
        exhibitionid: '',
        exhibitiontime: '',
        exhibitionintroduction: '',
        exhibitionlocation: '',
        exhibitiontel: '',
        exhibitionthinglist: '',
        exhibition_picture: '',
        status: ''
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
        museumid: '',
        exhibitionid: '',
        exhibitiontime: '',
        exhibitionintroduction: '',
        exhibitionlocation: '',
        exhibitiontel: '',
        exhibitionthinglist: '',
        exhibition_picture: '',
        status: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      addFormRules: {
        museumid: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        exhibitionid: [{ required: true, message: '请输入展览ID', trigger: 'blur' }],
        exhibitiontheme: [{ required: true, message: '请输入展览主题', trigger: 'blur' }],
        status: [{ required: true, message: '请输入状态', trigger: 'blur' }]
      },
      editForm: {
        museumid: '',
        exhibitionid: '',
        exhibitiontime: '',
        exhibitionintroduction: '',
        exhibitionlocation: '',
        exhibitiontel: '',
        exhibitionthinglist: '',
        exhibition_picture: '',
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

    fetchData() {
      this.listLoading = true
      getExhibitionList().then(response => {
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
    handleDeleteList: function(idnex, row) {
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
    } // end 删除

  }
}
</script>
