import { createContext, useState, ReactNode } from "react";

// AuthContextType defines the shape of the authentication context, including the user, token, and functions to update them.
interface AuthContextType {
    // user and token are initialized as null, and setUser and setToken are functions that will be used to update the user and token state in the context.
    user: string | null;
    token: string | null;
    setUser: (user: string | null) => void;
    setToken: (token: string | null) => void;
}

// Instance of AUthContext created with default values for user and token as null
// This will be implemented in AuthProvider component which update the Autentication state and provide it to the rest of the application.
export const AuthContext = createContext<AuthContextType>({
    user: null,
    token: null,
    setUser: () => {},
    setToken: () => {},
});

// Props interface defines the type for the children prop that will be passed to the AuthProvider.
interface Props {
    // children of type ReactNode allows for any valid React child elements to be passed to the AuthProvider comopnent.
    children: ReactNode;
}

export const AuthProvider: React.FC<Props> = ({ children }) => {
    // useState hooks are used to manage the user and token state within the AuthProvider component.
    const [user, setUser] = useState<string | null>(null);
    const [token, setToken] = useState<string | null>(null);

    return (
        // The AuthContext.Provider component is used to wrap the children components and provide them with access to the authentication state and functions defined in the context.
        <AuthContext.Provider value={{ user, token, setUser, setToken }}>
            {children}
        </AuthContext.Provider>
    );
}