import { createStore, applyMiddleware, compose } from 'redux'
import thunk from 'redux-thunk'
import storage from 'redux-persist/lib/storage'
import { persistStore, persistReducer } from 'redux-persist'
import autoMergeLevel2 from 'redux-persist/lib/stateReconciler/autoMergeLevel2'
import rootReducer from '../reducers/indexx'

const composeEnhancers =
  (window as any).__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const persistConfig = {
  key: 'root',
  storage: storage,
  stateReconciler: autoMergeLevel2, // 查看 'Merge Process' 部分的具体情况
}

const PersistReducer = persistReducer(persistConfig, rootReducer)
const store = createStore(
  PersistReducer,
  composeEnhancers(applyMiddleware(thunk))
)
export const persistor = persistStore(store)
export default store
