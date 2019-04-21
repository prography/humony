import React from 'react';
import styled from 'styled-components';


const Btn = styled.button`
    padding: 10px 50px;
    border: none;
    border-radius: 30px;
    font-size: .9rem;
    font-weight: bold;
    box-shadow: $box-shadow-2;
    transition: box-shadow .5s;
    background: #fff;
    color: #333;
`;

const StartBtn:React.SFC = () => {
    return <Btn className="startBtn"><span>START</span> 지금 바로 시작하기</Btn>;
};
// const StartBtn = () => {
//     return (
//         <div>1</div>
//     );
// }
export default StartBtn;