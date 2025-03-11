import { useEffect, useState } from "react";
import Register from "./components/register";

const API_BASE_URL = "http://localhost:5000"; // Replace with your actual API
const ENDPOINTS = ["bets", "groups", "matches", "sports", "tournaments", "users"];

const App = () => {
  const [data, setData] = useState<Record<string, any>>({});
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    let results: Record<string, any> = {};

    try {
      const responses = await Promise.all(
        ENDPOINTS.map(endpoint => fetch(`${API_BASE_URL}/${endpoint}`))
      );
      
      const jsonData = await Promise.all(responses.map(res => res.json()));
      ENDPOINTS.forEach((endpoint, index) => {
        results[endpoint] = jsonData[index];
      });
      
      setData(results);
    } catch (err) {
      setError("Failed to fetch data");
    } finally {
      setLoading(false);
    }
  };

    return (
      <div>
        <div style={{ padding: "16px" }}>
          <h1 style={{ fontSize: "24px", fontWeight: "bold", marginBottom: "16px" }}>API Data Viewer</h1>
          <button onClick={fetchData} disabled={loading} style={{ marginBottom: "16px", padding: "8px 16px", cursor: "pointer" }}>
            {loading ? "Loading..." : "Refresh Data"}
          </button>
          {error && <p style={{ color: "red" }}>{error}</p>}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px" }}>
            {ENDPOINTS.map(endpoint => (
              <div key={endpoint} style={{ border: "1px solid #ccc", padding: "16px", borderRadius: "8px" }}>
                <h2 style={{ fontSize: "20px", fontWeight: "bold" }}>{endpoint}</h2>
                <pre style={{ fontSize: "14px", background: "#f5f5f5", padding: "8px", borderRadius: "4px", overflowX: "auto" }}>
                  {JSON.stringify(data[endpoint], null, 2) || "No data"}
                </pre>
              </div>
            ))}
          </div>
        </div>
        <Register />
      </div>
    );



};

export default App;