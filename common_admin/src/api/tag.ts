import request from '@utils/request'

export const queryAllTags = () =>
  request({
    url: `tag/all_tag`,
    method: 'get',
  })
