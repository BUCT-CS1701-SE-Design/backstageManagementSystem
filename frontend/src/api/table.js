import request from '@/utils/request'

export function getList(params) {
  return request({
    url: 'test',
    method: 'get',
    params
  })
}

export function letMuseumAdd(params) {
  return request({
    url: 'museumadd',
    method: 'post',
    params
  })
}

export function letMuseumDelete(params) {
  return request({
    url: 'museumdeleted',
    method: 'post',
    params
  })
}

export function letMuseumChange(params) {
  return request({
    url: 'museumchange',
    method: 'post',
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

export function letExhibitionAdd(params) {
  return request({
    url: 'exhibitionadd',
    method: 'post',
    params
  })
}

export function letExhibitionDelete(params) {
  return request({
    url: 'exhibitiondelete',
    method: 'post',
    params
  })
}

export function letExhibitionChange(params) {
  return request({
    url: 'exhibitionchange',
    method: 'post',
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

export function letCollectionAdd(params) {
  return request({
    url: 'collectionadd',
    method: 'post',
    params
  })
}

export function letCollectionDelete(params) {
  return request({
    url: 'collectiondelete',
    method: 'post',
    params
  })
}

export function letCollectionChange(params) {
  return request({
    url: 'collectionchange',
    method: 'post',
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

export function letCommentAdd(params) {
  return request({
    url: 'commentadd',
    method: 'post',
    params
  })
}

export function letCommentDelete(params) {
  return request({
    url: 'commentdelete',
    method: 'post',
    params
  })
}

export function letCommentChange(params) {
  return request({
    url: 'commentchange',
    method: 'post',
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
export function letexplainationsAdd(params) {
  return request({
    url: 'explanationadd',
    method: 'post',
    params
  })
}
export function letexplainationsDelete(params) {
  return request({
    url: 'explanationdelete',
    method: 'post',
    params
  })
}
export function letexplainationsChange(params) {
  return request({
    url: 'explanationchange',
    method: 'post',
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

export function letuserAdd(params) {
  return request({
    url: 'usersadd',
    method: 'post',
    params
  })
}

export function letuserDelete(params) {
  return request({
    url: 'usersdelete',
    method: 'post',
    params
  })
}

export function letuserChange(params) {
  return request({
    url: 'userschange',
    method: 'post',
    params
  })
}