// src/app/posts/page.tsx
import { useEffect, useState } from 'react';

export default function Posts() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/posts/')  // Django 데이터 API 호출
            .then(response => response.json())
            .then(data => setPosts(data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h1>게시판</h1>
            <ul>
                {posts.map((post: any) => (
                    <li key={post.id}>{post.title} - {post.author}</li>
                ))}
            </ul>
        </div>
    );
}