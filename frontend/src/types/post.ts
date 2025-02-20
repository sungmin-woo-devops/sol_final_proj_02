// src/types/post.ts
export interface Post {
  id: number;
  title: string;
  author: string;
  created_at: string;  // ISO 8601 형식 또는 문자열로 가정
}