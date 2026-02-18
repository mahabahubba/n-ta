import { useState } from "react";
import { Login } from "./components/Auth/Login";
import { Register } from "./components/Auth/Register";
import { AuthContext } from "./context/AuthContext";
import { Me } from "./pages/Me";

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
          <>
            <h2>Welcome, {user}</h2>
            <p>You’re logged in! You can now access protected routes.</p>

            <button
              onClick={() => {
                setToken(null);
                setUser(null);
              }}
              style={{ marginBottom: "1rem" }}
            >
              Logout
            </button>

            <hr />

            <Me />
          </>
        )}
      </div>
    </AuthContext.Provider>
  );
}

export default App;

