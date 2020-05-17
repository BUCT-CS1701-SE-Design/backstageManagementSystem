import request from '@/utils/request'

export function login(data) {
  return request({
    url: 'loginin',
    method: 'post',
    data
  })
}
// export function login(data) {
//   return request({
//     url: '/vue-admin-template/user/login',
//     method: 'post',
//     data
//   })
// }

export function getInfo(token) {
  return request({
    url: 'info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: 'loginout',
    method: 'post'
  })
}
