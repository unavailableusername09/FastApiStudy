<script>

    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'


    let question_list = []
    let page_index = 0
    let total = 0
    let total_page_list = Array(Math.ceil(total/10))
    $: total_page = Math.ceil(total/10)

    function get_question_list(_page) {
        let params = {
            page_index: _page
        }
        fastapi('get', '/api/question/list',params, (json) => {
            question_list = json.question_list
            page_index = _page
            total = json
        })
        
    }
    

    get_question_list(0)
</script>

<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {page_index <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page_index-1)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each total_page_list as loop_page}
        {console.log(loop_page)}
            <li class="page-item {loop_page === page_index && 'active'}">
                <button on:click="{() => get_question_list(loop_page)}" class="page-link">{loop_page+1}</button>
            </li>
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {page_index >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page_index+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>
