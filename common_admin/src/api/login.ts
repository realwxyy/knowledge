import request from '@utils/request'

export const login = (data: any) =>
  request({
    url: `login/login`,
    method: 'post',
    data,
  })
