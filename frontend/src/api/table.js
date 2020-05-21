import request from '@/utils/request'

export function getList(params) {
  return request({
    url: 'test',
    method: 'get',
    params
  })
}
export function getExhibitionList(params) {
  return request({
    url: '/exhibitionAll',
    method: 'get',
    params
  })
}
export function getNewsList(params) {
  return request({
    url: 'news',
    method: 'get',
    params
  })
}
export function getCollectionList(params) {
  return request({
    url: 'collection_All',
    method: 'get',
    params
  })
}
export function getCommentList(params) {
  return request({
    url: 'comment_All',
    method: 'get',
    params
  })
}

export function getexplainationsList(params) {
  return request({
    url: 'explanationtest',
    method: 'get',
    params
  })
}

export function getuserList(params) {
  return request({
    url: 'userstest',
    method: 'get',
    params
  })
}
