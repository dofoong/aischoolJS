let date = new Date();

const renderCalender = () => {
    const viewYear = date.getFullYear(); //올해
    const viewMonth = date.getMonth(); //이번달

    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

    const prevLast = new Date(viewYear, viewMonth, 0); //년 월 일 0은 1일 전날을 뜻하므로 전달 마지막 날
    const thisLast = new Date(viewYear, viewMonth + 1, 0); // 이번달 마지막 날

    const PLDate = prevLast.getDate(); //전 달의 마지막날 날자
    const PLDay = prevLast.getDay();// 전 달의 마지막날의 요일

    const TLDate = thisLast.getDate(); //이번달 마지막날
    const TLDay = thisLast.getDay(); // 이번달 마지막날의 요일

    const prevDates = []; // 달력 앞에 비는곳에 들어갈 배열
    const thisDates = [...Array(TLDate + 1).keys()].slice(1); // let thisDates = [...Array(TLDate).fill().map((ele, i) =>{return i + 1})];와
                                                            // 동일하게 동작하며 keys를 활용할경우 0부터 시작해 정수값에 1을 더해주고 배열이 만들어진후 앞에있는 0을 제거
                                                            // 6월 기준 return값은 [1,2,3....30]
    const nextDates = []; // 달력 뒤에 비는곳에 들어갈 배열

    if (PLDay !== 6){  
        for (let i = 0; i < PLDay + 1; i++){
            prevDates.unshift(PLDate - i);
        }
    }
    //getDay()는 일요일(0)부터 시작하여 토요일(6)으로 return값이 나옴 위 if문은 매 달 1일날이 일요일이 아닌경우 앞의 비는 칸을 채워주기 위한 것
    //PLDay(전달의 마지막날의 요일) === 6인 경우 이번달의 1일은 일요일 부터 시작이기에 위와같은 조건이 달림

    for (let i = 1; i < 7 - TLDay; i++){
        nextDates.push(i);
    }
    //이번달의 마지막 요일이 토요일(6)이 아닌경우 비는 값만큼 날을 생성 ex)22년 6월의 마지막 요일은 목요일(4) 이므로 2번 반복하여 1,2를 생성
    const dates = prevDates.concat(thisDates, nextDates); // 배열을 합치는 concat을 활용하여 prev this next 순으로 배열
    const firstDateIndex = dates.indexOf(1); // 합쳐진 배열(달력에 표기될 숫자들)에서 1일의 위치를 찾음
    const lastDateIndex = dates.lastIndexOf(TLDate); // 합쳐진 배열(달력에 표기될 숫자들)에서 그달의 마지막날 위치를 찾음
    dates.forEach((date, i) => {
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 
                          ? 'this'
                          : 'other';
        dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
    });
    // 이달의 날자일 경우 class명으로 this가 들어가고 전달이나 다음달일 경우 other가 들어감

    document.querySelector('.dates').innerHTML = dates.join('');

    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) { // 현재 보고있는 년월이 동일할경우
        for (let date of document.querySelectorAll('.this')) { // 모든 this 클래스중
            if (+date.innerText === today.getDate()) { // innerText로 작성된 날자와 오늘 날자가 동일할때 
                date.classList.add('today'); // 클래스명 today를 추가하여 css 파일에서 지정된 값을 받아옴
                break;
            }
        }
    }
}

renderCalender();

const prevMonth = () => {
    date.setDate(1); // 오늘 날자가 전달이나 다음달에 존재하지 않는경우 여러달이 지나버릴수 있는 경우를 위해 작성
    date.setMonth(date.getMonth() - 1);
    renderCalender();
};

const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() + 1);
    renderCalender();
};

const goToday = () => {
    date = new Date();
    renderCalender();
}

// 원본 : https://www.youtube.com/watch?v=jFmcH5GVRs4

// 접속위치가 어디든 한국의 시간을 불러오는 방법
// 1. UTC(협정 세계시)를 불러온다 
// let dt = new Date(); > let utc = dt.getTime() + (dt.getTimezoneOffset() * 60 * 1000); 
// 겟타임은 현재시간을 밀리초로 받아오며 타임존오프셋은 UTC가 로컬타임과 얼마나 차이나는지 분으로 반환 한국의 경우 9시간이니 -540이 반환됨
// 즉 타임존 오프셋을 밀리초로 변환 해주기 위해 *60 *1000 을 해주고 겟타임과 더해줄 경우 어느지역 에서도 UTC값이 반환됨
// 2. 기준인 UTC 와 한국의 시간은 9시간이 차이가 나니 그만큼 더해준다
// let findKR = 9 * 60 * 60 * 1000; > let KRtime = new Date(utc + findKR);  
// 9시간을 밀리초로 변환해준 findKR의 값을 기존에 구해둔 utc에 더하면 한국의 시간이 나오게 된다