import request from '@utils/request'

export const queryBrandList = (data: any) =>
  request({
    url: `brand/admin_list`,
    method: 'get',
    params: data,
  })
export const addBrand = (data: any) =>
  request({
    url: `brand/brand`,
    method: 'post',
    data,
  })

export const saveBrand = (data: any) =>
  request({
    url: `brand/brand`,
    method: 'put',
    data,
  })

export const delBrand = (data: any) =>
  request({
    url: `brand/brand`,
    method: 'delete',
    params: data,
  })

export const queryBrandDetail = (data: any) =>
  request({
    url: `brand/brand`,
    method: 'get',
    params: data,
  })
