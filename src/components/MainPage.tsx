import React from "react";

const MainPage: React.FC = () => {
  return (
    <div>
      <h2>Main Page</h2>
      <p>Welcome to the main page!</p>
      <button
        onClick={() => {
          alert("logout clicked");
        }}
      >
        Logout
      </button>
    </div>
  );
};

export default MainPage;
