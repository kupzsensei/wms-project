import { TitleContext } from "@/App";
import { FC, useContext, useEffect } from "react";

export const ProductPage: FC = () => {
const pageContext = useContext(TitleContext)

  useEffect(() => {
    if (pageContext) {
      pageContext.setPageTitle("Products");
    }
  }, []);
  return <h1>Hello from product page</h1>;
};
