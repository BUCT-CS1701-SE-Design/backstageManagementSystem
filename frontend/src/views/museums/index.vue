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

          <el-table-column align="center" label="ID" width="75">
            <template slot-scope="scope">
              {{ scope.row.pk }}
            </template>
          </el-table-column>

          <el-table-column label="博物馆名" width="300" align="center">
            <template slot-scope="scope">

              <el-button size="middle" @click="handleSelect(scope.row)">{{ scope.row.fields.museumname }}</el-button>

            </template>

          </el-table-column>

          <el-table-column label="地址" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.location }}</span>
            </template>
          </el-table-column>

          <el-table-column label="官网链接" align="center" width="200">
            <template slot-scope="scope">
              <a href="(scope.row.fields.link)"> {{ scope.row.fields.link }} </a>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="Status" width="80" align="center">
            <template slot-scope="scope">
              <el-tag :type="scope.row.fields.status | statusFilter">{{ scope.row.fields.status }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column align="center" prop="created_at" label="开放时间" width="300">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.fields.opentime }}</span>
            </template>
          </el-table-column>

          <el-table-column fixed="right" label="操作" align="center" width="200">
            <template slot-scope="scope">
              <el-button size="small" icon="el-icon-edit" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="small" @click="handleDeleteList(scope.row)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </template><!--页面表格结束-->

      <!-- 分页 -->
      <el-pagination :current-page="currentPage" :page-size="pageSize" layout="total, prev, pager, next" :total="count" @current-change="getResult" />
    </div>  <!---div class="app-container"结束-->

    <!--新增界面-->
    <el-dialog title="新增博物馆信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="ID" prop="museumID">
          <el-input v-model="addForm.museumID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="名称" prop="museumname">
          <el-input v-model="addForm.museumname" auto-complete="off" />
        </el-form-item>

        <el-form-item label="简介" prop="introduction">
          <el-input v-model="addForm.introduction" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="开放时间" prop="opentime">
          <el-input v-model="addForm.opentime" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="网址" prop="link">
          <el-input v-model="addForm.link" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="位置" prop="location">
          <el-input v-model="addForm.location" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="label" prop="label">
          <el-input v-model="addForm.label" auto-complete="off" />
        </el-form-item>

        <!--  <el-form-item label="新简介" prop="museum_introduction">
					<el-input v-model="addForm.museum_introduction" auto-complete="off"></el-input>
				</el-form-item>-->

        <el-form-item label="等级" prop="grade">
          <el-input v-model="addForm.grade" auto-complete="off" />
        </el-form-item>

        <el-form-item label="年参观量" prop="annual_visits">
          <el-input v-model="addForm.annual_visits" auto-complete="off" />
        </el-form-item>

        <el-form-item label="面积" prop="area">
          <el-input v-model="addForm.area" auto-complete="off" />
        </el-form-item>

        <el-form-item label="电话" prop="telephone">
          <el-input v-model="addForm.telephone" auto-complete="off" />
        </el-form-item>

        <el-form-item label="门票" prop="admission_fee">
          <el-input v-model="addForm.admission_fee" auto-complete="off" />
        </el-form-item>

        <el-form-item label="建设时间" prop="building_time">
          <el-input v-model="addForm.building_time" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品数量" prop="collection_number">
          <el-input v-model="addForm.collection_number" auto-complete="off" />
        </el-form-item>

        <el-form-item label="城市" prop="city">
          <el-input v-model="addForm.city" auto-complete="off" />
        </el-form-item>

        <el-form-item label="status" prop="status">
          <el-input v-model="addForm.status" auto-complete="off" />
        </el-form-item>

      </el-form>

      <!--提交或者取消-->
      <div slot="footer" class="dialog-footer">
        <el-button @click="addFormVisible = false">取消</el-button>
        <el-button type="primary" :loading="addLoading" @click="addSubmit">提交</el-button>

      </div>
    </el-dialog>
    <!--新增界面结束-->

    <!--详细界面-->
    <el-dialog title="详细信息" :visible.sync="selectFormVisible" :close-on-click-modal="false">
  <el-card>
      
  <div   class="text item">
     {{"博物馆ID: "+selectForm.museumid}}
     <br><br>
    {{"博物馆名称:  "+selectForm.museumname}}
      <br><br>
      {{"简介： "+selectForm.introduction}}
       <br><br>
       {{"开放时间： "+selectForm.opentime}}
        <br><br>
        {{"网址： "+selectForm.link}}
        <br><br>
        {{"位置: "+selectForm.location}}
         <br><br>
         {{"label: "+selectForm.label}}
         <br><br>
         {{"等级: "+selectForm.grade}}
         <br><br>
         {{"年参观量: "+selectForm.annual_visits}}
         <br><br>
         {{"面积: "+selectForm.area}}
         <br><br>
         {{"电话: "+selectForm.telephone}}
           <br><br>
         {{"门票: "+selectForm.admission_fee}}
           <br><br>
         {{"建设时间: "+selectForm.building_time}}
           <br><br>
         {{"藏品数量: "+selectForm.collection_number}}
          <br><br>
         {{"城市: "+selectForm.city}}
          <br><br>
         {{"status: "+selectForm.status}}


  </div>
</el-card>


      
    </el-dialog> <!--详细界面结束-->

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form ref="editForm" :inline="true" :model="editForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="ID" prop="museumID">
          <el-input v-model="editForm.museumID" auto-complete="off" />
        </el-form-item>

        <el-form-item label="名称" prop="museumname">
          <el-input v-model="editForm.museumname" auto-complete="off" />
        </el-form-item>

        <el-form-item label="简介" prop="introduction">
          <el-input v-model="editForm.introduction" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="开放时间" prop="opentime">
          <el-input v-model="editForm.opentime" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="网址" prop="link">
          <el-input v-model="editForm.link" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="位置" prop="location">
          <el-input v-model="editForm.location" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="label" prop="label">
          <el-input v-model="editForm.label" auto-complete="off" />
        </el-form-item>

        <el-form-item label="等级" prop="grade">
          <el-input v-model="editForm.grade" auto-complete="off" />
        </el-form-item>

        <el-form-item label="年参观量" prop="annual_visits">
          <el-input v-model="editForm.annual_visits" auto-complete="off" />
        </el-form-item>

        <el-form-item label="面积" prop="area">
          <el-input v-model="editForm.area" auto-complete="off" />
        </el-form-item>

        <el-form-item label="电话" prop="telephone">
          <el-input v-model="editForm.telephone" auto-complete="off" />
        </el-form-item>

        <el-form-item label="门票" prop="admission_fee">
          <el-input v-model="editForm.admission_fee" auto-complete="off" />
        </el-form-item>

        <el-form-item label="建设时间" prop="building_time">
          <el-input v-model="editForm.building_time" auto-complete="off" />
        </el-form-item>

        <el-form-item label="藏品数量" prop="collection_number">
          <el-input v-model="editForm.collection_number" auto-complete="off" />
        </el-form-item>

        <el-form-item label="城市" prop="city">
          <el-input v-model="editForm.city" auto-complete="off" />
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
import { getList } from '@/api/table'

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
        museumID: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        museumname: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      // 新增界面数据
      addForm: {
        museumID: '',
        museumname: '',
        introduction: '',
        opentime: '',
        link: '',
        location: '',
        label: '',
        //  museum_introduction: "",
        grade: '',
        annual_visits: '',
        area: '',
        telephone: '',
        admission_fee: '',
        building_time: '',
        collection_number: '',
        city: '',
        status: ''
      },

      // 查看详细信息页面是否显示
      selectFormVisible: false,
      selectForm: {
        museumID: '',
        museumname: '',
        introduction: '',
        opentime: '',
        link: '',
        location: '',
        label: '',
        //  museum_introduction: "",
        grade: '',
        annual_visits: '',
        area: '',
        telephone: '',
        admission_fee: '',
        building_time: '',
        collection_number: '',
        city: '',
        status: ''
      },

      // 编辑界面是否显示
      editFormVisible: false,
      // 添加按钮Loading加载
      editLoading: false,
      // 编辑规则
      addFormRules: {
        museumID: [{ required: true, message: '请输入博物馆ID', trigger: 'blur' }],
        museumname: [{ required: true, message: '请输入博物馆名称', trigger: 'blur' }],
        status: [{ required: true, message: '请输入博物馆状态', trigger: 'blur' }]
      },
      editForm: {
        museumID: '',
        museumname: '',
        introduction: '',
        opentime: '',
        link: '',
        location: '',
        label: '',
        grade: '',
        annual_visits: '',
        area: '',
        telephone: '',
        admission_fee: '',
        building_time: '',
        collection_number: '',
        city: '',
        status: ''
      }
    }// end return
  },

  created() {
    this.fetchData()
  },
  methods: {

    // getResult: function(val) {
    //   var _this = this
    //   this.listLoading = true
    //   const param = Object.assign(
    //     {},
    //     {
    //       currentPage: val,
    //       pageSize: 10
    //     }
    //   )
    //   this.$ajax({
    //     method: 'post',
    //     url: '/exhibajax',
    //     data: param
    //   }).then(function(resultData) {
    //     _this.tableData = resultData.data.data
    //     _this.count = resultData.data.count
    //     _this.listLoading = false
    //   })
    // },

    fetchData() {
      this.listLoading = true
      getList().then(response => {
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
