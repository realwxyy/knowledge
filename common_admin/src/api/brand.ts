import request from '@utils/request'

export const queryBrandList = (data: any) =>
  request({
    url: `brand/admin_list`,
    method: 'get',
    params: data,
  })
