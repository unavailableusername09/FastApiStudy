<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  // @ts-ignore
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from "./components/Navigation.svelte"
  import UserCreate from "./routes/UserCreate.svelte"
  import UserLogin from "./routes/UserLogin.svelte"

  const routes = {
    '/': Home,
    '/detail/:question_id': Detail,
    '/question-create' : QuestionCreate,
    '/user-create': UserCreate,
    '/user-login': UserLogin,
  }
</script>

<Navigation />
<Router {routes}/>
