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
} export function getNewsList(params) {
  return request({
    url: 'test',
    method: 'get',
    params
  })
} export function getCollectionList(params) {
  return request({
    url: 'test',
    method: 'get',
    params
  })
}
