import { useEffect, useState } from "react";
import { Login } from "./components/Auth/Login";
import { Register } from "./components/Auth/Register";
import { AuthContext } from "./context/AuthContext";
import { Me } from "./pages/Me";
import { useNotifications } from "./hooks/useNotifications";

function App() {
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("token")
  );
  const [user, setUser] = useState<string | null>(
    localStorage.getItem("user")
  );

  // Persist token in localStorage
  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);
    } else {
      localStorage.removeItem("token");
    }
  }, [token]);

  // Persist user in localStorage
  useEffect(() => {
    if (user) {
      localStorage.setItem("user", user);
    } else {
      localStorage.removeItem("user");
    }
  }, [user]);

  // Hook for real-time notifications
  const notifications = useNotifications(token);

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
            <button
              onClick={() => {
                setToken(null);
                setUser(null);
                localStorage.clear();
              }}
            >
              Logout
            </button>

            <hr />

            {/* Protected /me route */}
            <Me />

            {/* Notifications */}
            {notifications.length > 0 && (
              <div style={{ marginTop: "1rem" }}>
                <h3>Notifications</h3>
                <ul>
                  {notifications.map((note, idx) => (
                    <li key={idx}>{note}</li>
                  ))}
                </ul>
              </div>
            )}
          </>
        )}
      </div>
    </AuthContext.Provider>
  );
}

export default App;
