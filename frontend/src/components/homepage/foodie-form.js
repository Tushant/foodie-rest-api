import React, { Component } from 'react';

class FoodieForm extends Component {
	render() {
		return (
			 <div className="ui segment foodie-form">
	           <div className="ui equal width grid center aligned">
	           	<div className="ui fluid cards foodie-form-card">
	           		<div className="card">
	           			<div className="content">
	           				<div className="ui form description">
	           					<div className="field">
						           	<h1 className="form-quote">
						              	<span>I feel like having</span>
						              	<span>
						              		<select className="ui fluid dropdown">
						              			<option value="DI">Dinner</option>
											    <option value="LU">Lunch</option>
											    <option value="BR">Breakfast</option>
											    <option value="LX">Luxury</option>
						              		</select>
						              	</span>
						              	<span>
						              		in
						              		<select className="ui fluid dropdown">
						              			<option value="DI">Koteshwor</option>
											    <option value="LU">Baneshwor</option>
						              		</select>
						              	</span> <br /> <br />
						              	<button className="massive ui button find">
										  <span><i className="search icon"></i></span>Find A Restaurant
										</button>
						             </h1>
						        </div>
					        </div>
			             </div>
			        </div>
	           	</div>
	           </div>
	          </div>
			);
	}
}

export default FoodieForm;