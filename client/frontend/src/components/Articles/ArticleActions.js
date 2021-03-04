import axios from "axios";
import {toastOnError} from "../../utils/Utils";
import {GET_ARTICLES,ADD_ARTICLE} from "./ArticleTypes";


export const getArticles=()=>dispatch=>{
    axios.get("/api/showall/")
    .then(response=>{
        dispatch({
            type:GET_ARTICLES,
            payload:response.data
        });
    })
    .catch(error=>{
        toastOnError(error);
    });
}


export const addArticle=article=>dispatch=>{
    axios.post("/api/article/",article)
    .then(response=>{
        dispatch({
            type:ADD_ARTICLE,
            payload:response.data
        })
    })
    .catch(error=>{
        toastOnError(error);
    })
}