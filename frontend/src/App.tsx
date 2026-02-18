import { useState } from "react";
import { Login } from "./components/Auth/Login";
import { AuthContext } from "./context/AuthContext";
import { Register } from "./components/Auth/Register";

function App() {
  const [token, setToken] = useState<string | null>(null);
  const [user, setUser] = useState<string | null>(null);

  return (
    <AuthContext.Provider value={{ token, setToken, user, setUser }}>
      <div style={{ padding: "2rem" }}>
        <h1>N-TA Frontend</h1>
        {!token ? (
          <>
            <h2>Register</h2>
            <Register />
            <h2>Login</h2>
            <Login />
          </>
        ) : (
          <div>
            <h2>Welcome, {user}</h2>
            <p>You’re logged in! You can now access protected routes.</p>
          </div>
        )}
      </div>
    </AuthContext.Provider>
  );
}

export default App;
