<template>
  <section>

    <div class="app-container">

      <!-- 搜索区begin -->
      <div class="handle-box">
        <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
          <el-form :inline="true" :model="ff">
            <!----> <el-form-item>
                      博物馆ID： <el-input v-model="ff.museumid" placeholder="博物馆ID" style="width:200px; heght:30px;" size="mini" />
                    </el-form-item>

            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="mini" @click="getResult()">搜索</el-button>
            </el-form-item>

          </el-form>
        </el-col>
      </div>   <!--搜索区end -->

      <!--新增按钮-->
      <div>
        <el-button type="success" icon="el-icon-circle-plus-outline" size="mini" round @click="handleAdd">新增</el-button>
      </div>

      <!--页面表格显示信息--->
      <template>
        <el-table v-loading="listLoading" :data="list" element-loading-text="Loading" border fit highlight-current-row>

          <el-table-column align="center" label="博物馆ID" width="105">
            <template slot-scope="scope">
              {{ scope.row.fields.museumid }}
            </template>
          </el-table-column>

          <el-table-column label="新闻标题" width="200" align="center">
            <template slot-scope="scope">{{ scope.row.fields.newstitle | ellipsis10 }}
              <el-button size="middle" mulitline="true" @click="handleSelect(scope.row)">详情</el-button>
            </template>
          </el-table-column>

          <el-table-column label="时间" align="center">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.fields.newstime }}</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="新闻类别" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.positive_negative }}</span>
            </template>
          </el-table-column>

          <el-table-column label="内容" align="center" width="300">
            <template slot-scope="scope">
              <a href=""> {{ scope.row.fields.newsmaintext | ellipsis20 }} </a>
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
    <el-dialog title="新增新闻信息" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form ref="addForm" :inline="true" :model="addForm" label-width="80px" :rules="addFormRules">

        <el-form-item label="博物馆ID" prop="museumid">
          <el-input v-model="addForm.museumid" auto-complete="off" />
        </el-form-item>

        <el-form-item label="新闻标题" prop="newstitle">
          <el-input v-model="addForm.newstitle" type="textarea" auto-complete="off" />
        </el-form-item>

        <el-form-item label="新闻时间" prop="newstime">
         <el-date-picker  v-model="addForm.newstime" type="date"  placeholder="选择日期" value-format="yyyy-MM-dd"></el-date-picker> 
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
        <el-button type="primary" @click="addSubmit" :loading="addLoading">提交</el-button>
        
      </div>
    </el-dialog>
    <!--新增界面结束-->

    <!--详细界面-->
    <el-dialog title="详细信息" :visible.sync="selectFormVisible" :close-on-click-modal="false">
       <el-card>
      
  <div   class="text item">
     {{"博物馆ID: "+selectForm.museumid}}
     <br><br>
    {{"博物馆名称:  "}}  {{selectForm.museumid|museumIDfilter}}
      <br><br>
      {{"新闻标题： "+selectForm.newstitle}}
       <br><br>
       {{"时间： "+selectForm.newstime}}
        <br><br>
        {{"性质： "+selectForm.positive_negative}}
        <br><br>
        {{"内容: "+selectForm.newsmaintext}}
         <br><br>
         {{"status: "+selectForm.status}}
  </div>
</el-card>

      
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
    },

     ellipsis10(value) {
      if (!value) return "";
      if (value.length > 10) {
        return value.slice(0, 10) + "...";
      }
      return value;
    },

    ellipsis20(value) {
      if (!value) return "";
      if (value.length > 20) {
        return value.slice(0, 20) + "...";
      }
      return value;
    },
     museumIDfilter(MID) {
      const IDMap = {
        1:	'故宫博物院',
        2:	'中国科学技术馆',
        3:	'中国地质博物馆',
        4:	'中国人民革命军事博物馆',
        5:	'中国航空博物馆',
        6:	'北京鲁迅博物馆',
        7:	'首都博物馆',
        8:	'北京自然博物馆',
        9:	'中国人民抗日战争纪念馆',
        10:	'周口店遗址博物馆',
        11:	'中国国家博物馆',
        12:	'中国农业博物馆',
        13:	'北京天文馆',
        14:	'恭王府',
        15:	'天津博物馆',
        16:	'天津自然博物馆',
        17:	'周恩来邓颖超纪念馆',
        18:	'河北博物院',
        19:	'西柏坡纪念馆',
        20:	'邯郸市博物馆',
        21:	'山西博物院',
        22:	'中国煤炭博物馆',
        23:	'八路军太行纪念馆',
        24:	'内蒙古博物院',
        25:	'鄂尔多斯博物馆',
        26:	'辽宁省博物馆',
        27:	'“九·一八”历史博物馆',
        28:	'旅顺博物馆',
        29:	'沈阳故宫博物院',
        30:	'大连现代博物馆',
        31:	'吉林省自然博物馆',
        32:	'吉林省博物院',
        33:	'伪满皇宫博物院',
        34:	'东北烈士纪念馆',
        35:	'大庆铁人王进喜纪念馆',
        36:	'瑷珲历史陈列馆',
        37:	'黑龙江省博物馆',
        38:	'大庆博物馆',
        39:	'上海博物馆',
        40:	'上海鲁迅纪念馆',
        41:	'中国共产党第一次全国代表大会会址纪念馆',
        42:	'上海科技馆',
        43:	'上海鲁迅纪念馆',
        44:	'南京博物院',
        45:	'侵华日军南京大屠杀遇难同胞纪念馆',
        46:	'南通博物苑',
        47:	'苏州博物馆',
        48:	'扬州博物馆',
        49:	'常州博物馆',
        50:	'南京市博物总馆',
        51:	'浙江省博物馆',
        52:	'温州博物馆',
        53:	'浙江自然博物院',
        54:	'中国丝绸博物馆',
        55:	'宁波博物馆',
        56:	'杭州博物馆',
        57:	'安徽博物院',
        58:	'安徽中国徽州文化博物馆',
        59:	'福建博物院',
        60:	'古田会议纪念馆',
        61:	'泉州海外交通史博物馆',
        62:	'中国闽台缘博物馆',
        63:	'中央苏区（闽西）历史博物馆',
        64:	'井冈山革命博物馆',
        65:	'江西省博物馆',
        66:	'中央革命根据地纪念馆',
        67:	'八一南昌起义纪念馆',
        68:	'安源路矿工人运动纪念馆',
        69:	'青岛市博物馆',
        70:	'中国甲午战争博物馆',
        71:	'青州市博物馆',
        72:	'山东博物馆',
        73:	'烟台市博物馆',
        74:	'潍坊市博物馆',
        75:	'河南博物院',
        76:	'郑州博物馆',
        77:	'洛阳博物馆',
        78:	'汉画馆',
        79:	'开封博物馆',
        80:	'鄂豫皖苏区首府革命博物馆',
        81:	'湖北省博物馆',
        82:	'荆州博物馆',
        83:	'武汉博物馆',
        84:	'辛亥革命武昌起义纪念馆',
        85:	'武汉中山舰博物馆',
        86:	'湖南省博物馆',
        87:	'韶山毛泽东故居纪念馆',
        88:	'刘少奇故居纪念馆',
        89:	'长沙简牍博物馆',
        90:	'广东省博物馆',
        91:	'西汉南越王博物馆',
        92:	'孙中山故居纪念馆',
        93:	'深圳博物馆',
        94:	'广州博物馆',
        95:	'广东民间工艺博物馆',
        96:	'广西壮族自治区博物馆',
        97:	'广西民族博物馆',
        98:	'海南省博物馆',
        99:	'自贡恐龙博物馆',
        100:	'三星堆博物馆',
        101:	'成都武侯祠博物馆',
        102:	'邓小平故居陈列馆',
        103:	'成都杜甫草堂博物馆',
        104:	'四川博物院',
        105:	'成都金沙遗址博物馆',
        106:	'自贡市盐业历史博物馆',
        107:	'遵义会议纪念馆',
        108:	'云南省博物馆',
        109:	'云南名族博物馆',
        110:	'重庆中国三峡博物馆',
        111:	'重庆红岩历史博物馆',
        112:	'重庆自然博物馆',
        113:	'西藏博物馆',
        114:	'陕西历史博物馆',
        115:	'秦始皇帝陵兵马俑博物馆',
        116:	'延安革命纪念馆',
        117:	'汉阳陵博物馆',
        118:	'西安碑林博物馆',
        119:	'西安半坡博物馆',
        120:	'西安博物院',
        121:	'宝鸡青铜器博物院',
        122:	'大唐西市博物馆',
        123:	'甘肃省博物馆',
        124:	'天水市博物馆',
        125:	'敦煌研究院',
        126:	'宁夏固原博物馆',
        127:	'宁夏回族自治区博物馆',
        128:	'青海省博物馆',
        129:	'新疆维吾尔自治区博物馆',
        130:	'吐鲁番博物馆',
        300:	'120testname'

      }
      return IDMap[MID]
    }


  },
  data() {
    return {
      list: null,
      listLoading: true,

      ff: {
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
      var _this = this
      this.listLoading = true
      const param = Object.assign(
        {},
        {
          museumid: this.ff.museumid
        }
      )
      this.$ajax({
        method: 'get',
        url: 'news',
        data: param
      }).then(function(response) {
        _this.ff = response.data.items.fields
        _this.listLoading = false
      })
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
