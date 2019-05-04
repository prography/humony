import React from 'react';
import PageTemplate from '../components/common/PageTemplate';
import Home from '../components/Home';


const MainPage: React.FC = () => {
    return (
        <PageTemplate>
            <Home/>
        </PageTemplate>
    );
};

export default MainPage;