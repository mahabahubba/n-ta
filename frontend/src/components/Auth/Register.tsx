import {useState, FormEvent, useContext} from "react";
import { AuthContext } from "../../context/AuthContext";
import { registerUser } from "../../api/auth";

export const Register = () => {
    const { setUser, setToken } = useContext(AuthContext);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState<string | null>(null);

    const handleRegister = async (e: React.SyntheticEvent<HTMLFormElement>) => {
        e.preventDefault();
        setError(null)
        try {
            const res = await fetch("http://localhost:8000/api/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            });

            if (!res.ok) {
                const data = await res.json();
                throw new Error(data.detail || "Registration failed");
            }
           
            const loginRes = await fetch("http://localhost:8000/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            });

            if (!loginRes.ok) {
                const data = await loginRes.json();
                throw new Error(data.detail || "Login after registration failed");
            }

            const loginData = await loginRes.json();
            setUser(email);
            setToken(loginData.access_token);
        } catch (err) {
            setError("Registration failed");
        }
    }

    
  return (
    <form onSubmit={handleRegister} style={{ marginBottom: "1rem" }}>
      <div>
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <button type="submit">Register</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );


}