import { createContext, useState } from "react";
import { AppSidebar } from "./components/app-sidebar";
import { SidebarProvider, SidebarTrigger } from "./components/ui/sidebar";
import { Outlet } from "react-router-dom";

interface titleContextType {
  setPageTitle: React.Dispatch<React.SetStateAction<string>>;
  pageTitle: string;
}

export const TitleContext = createContext<titleContextType | undefined>(undefined) 

function App() {
  const [pageTitle, setPageTitle] = useState("Dashboard");
  return (
    <SidebarProvider>
      <AppSidebar />
      <main className="flex flex-col gap-5 p-5">
        <div className="flex gap-3 items-center">
          <SidebarTrigger />
          <h1 className="font-bold">{pageTitle}</h1>
        </div>
        <TitleContext.Provider value={{pageTitle , setPageTitle}}>
          <Outlet />
        </TitleContext.Provider>
      </main>
    </SidebarProvider>
  );
}

export default App;
