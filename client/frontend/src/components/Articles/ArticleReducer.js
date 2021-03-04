import {GET_ARTICLES,ADD_ARTICLE} from "./ArticleTypes";

const initialState={
    articles:[]
};

export const articlesReducer=(state=initialState,action)=>{
    switch(action.type){
        case GET_ARTICLES:
            return{
                ...state,
                articles:action.payload
            };
        case ADD_ARTICLE:
            return {
                ...state,
                articles:[...state.articles,action.payload]
            };
        default:
            return state;
    }
}