import { Post } from '@/types/post';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';

async function getPosts() {
    const res = await fetch('http://localhost:8000/api/dashboard/', {
        headers: {
            'Accept': 'application/json',
        },
    });
    if (!res.ok) throw new Error('Failed to fetch posts');
    const data = await res.json();
    return data.posts as Post[];
}

export default async function Dashboard() {
    const posts = await getPosts();

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-3xl font-bold mb-6">대시보드</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {posts.map((post) => (
                    <Card key={post.id}>
                        <CardHeader>
                            <CardTitle>{post.title}</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <p>작성자: {post.author}</p>
                            <p className="text-sm text-muted-foreground">
                                작성일: {new Date(post.created_at).toLocaleDateString()}
                            </p>
                        </CardContent>
                    </Card>
                ))}
            </div>
            {posts.length === 0 && <p className="text-center text-muted-foreground">게시글이 없습니다.</p>}
        </div>
    );
}