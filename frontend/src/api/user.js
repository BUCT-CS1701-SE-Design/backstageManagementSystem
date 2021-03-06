import request from '@/utils/request'
export function get_csrf() {
  return request({
    url: 'get_csrf',
    method: 'get'
  })
}
export function login(data) {
  // const csrf_token = get_csrf()
  return request({
    url: 'loginin',
    method: 'post',
    // headers: { 'Content-Type': 'multipart/form-data', 'X-CSRFToken': csrf_token },
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
