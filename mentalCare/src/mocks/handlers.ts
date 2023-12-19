import { http, HttpResponse } from 'msw'

const all_posts = new Map<string, string>()
all_posts.set("taro", "hey")
all_posts.set("hanako", "hello")


export const handlers = [
  http.get('/hello', () => {
    return HttpResponse.json(Array.from(all_posts.values()))
  })
]