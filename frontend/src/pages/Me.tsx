import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import { fetchMe } from "../api/user";

type MeReponse = {
    id: number;
    email: string;
}

export const Me = () => {
    const { token } = useContext(AuthContext);
    const [user, setUser] = useState<MeReponse | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        if(!token) {
            setError("No token found. Please log in.");
            setLoading(false);
            return;
        }

        fetchMe(token)
            .then(setUser)
            .catch((err) => {
                console.error("Failed to fetch user info:", err);
                setError("Failed to fetch user info");
            })
            .finally(() => setLoading(false));
    }, [token]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div>
        <h2>My Profile</h2>
        <p><strong>ID:</strong> {user?.id}</p>
        <p><strong>Email:</strong> {user?.email}</p>
        </div>
    );


}