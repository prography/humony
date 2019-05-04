import React, { ReactNode, Component } from 'react';
import Header from '../Header';
import Footer from '../Footer';

interface Props {
    children: ReactNode
}

interface State {
    scrollTop: number
}


class PageTemplate extends Component<Props, State> {
    state = {
        scrollTop: 0
    };
    componentDidMount = () => {
        window.addEventListener('scroll', this.WindowScroll);
    }

    shouldComponentUpdate (nextProps: Props, nextState: State): any {
        if (this.state.scrollTop <= 100 && nextState.scrollTop >= 100 || this.state.scrollTop >= 100 && nextState.scrollTop <= 100) {
            return true;
        } else {
            return false;
        }
    }
    
    WindowScroll  = () => {
        this.setState({
            scrollTop: document.documentElement.scrollTop
        });
    }

    render () {
        return (
            <div className="page-template">
             <Header scrollTop ={this.state.scrollTop} />
             <main>
                 {this.props.children}
             </main>
             <Footer />
         </div>
        );
    }
}

export default PageTemplate;